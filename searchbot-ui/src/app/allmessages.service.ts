import { Injectable } from '@angular/core';
import { MessageClass } from './messageclass';
import { ButtonManagerService } from './button-manager.service';
import { GetRasaResponceService } from './get-rasa-responce.service';
import { catchError } from 'rxjs/operators';
import { HttpErrorResponse } from '@angular/common/http'; 
import { EMPTY } from 'rxjs';
import { AtmLocationCardsService } from './atm-location-cards.service';

@Injectable({
  providedIn: 'root'
})
export class AllmessagesService {

	messages: MessageClass[] = [];
	
	public addMessageByBot(b: any[]): void {
		console.log(b);
		var copy: any[] = [];
		var locationsPresent: boolean = false;
		for(let data of b) {
			if(data.hasOwnProperty('buttons')) {
				this.btnManagerService.activateButton(data.buttons, false);
				copy.push(data);
				continue;
			}
			if(data.hasOwnProperty('custom')) {
				this.atmLocationCardService.pushLocation(data.custom);
				locationsPresent = true;
				continue;
			}
			copy.push(data);
		}
		this.messages.push({isbot: true, body: copy});
		if(locationsPresent)
            this.show4();
	}

	public show4(): void {
		var cards = this.atmLocationCardService.pop4();
		var cardobject: any[] = [];
		for(let card of cards)
			cardobject.push({'custom': card});
		console.log("cards are", cards);
		this.messages.push({isbot: true, body: cardobject});
		if(this.atmLocationCardService.hasLocationsLeft())
			this.btnManagerService.activateButton(
				[{
					'payload': null,
					'title': 'see more'
				}],
				true
			);
	}

	public addMessageByUser(b: string):void {
		if(this.btnManagerService.hasButtons())
			this.btnManagerService.deactivateButton();
		this.atmLocationCardService.emptyLocations();
		this.messages.push({isbot: false, body: b});
		this.rasaResponceService.sendMessage(b).pipe(
			catchError(
				(error: HttpErrorResponse) => {
					console.log(error);
					this.addMessageByBot(
						[{text: "Sorry, I can not reach to server right now. \
								Please check your internet connectivity and try again :("
						}]
					);
					return EMPTY;
				}
			)
		)
		.subscribe(
			(data: any) => {
				this.addMessageByBot(data);
			}
		);
	}

	public addMockMessageByUser(b: string, toShow: string): void {
		if(this.btnManagerService.hasButtons())
			this.btnManagerService.deactivateButton();
		this.messages.push({isbot: false, body: toShow});
		if(b != null) {
			this.rasaResponceService.sendMessage(b).pipe(
				catchError(
					(error: HttpErrorResponse) => {
						console.log(error);
						this.addMessageByBot(
							[{text: "Sorry, I can not reach to server right now. \
									Please check your internet connectivity and try again :("
							}]
						);
						return EMPTY;
					}
				)
			)
			.subscribe(
				(data: any) => {
					this.addMessageByBot(data);
				}
			);
		}
	}

	public totalMessages(): number {
		return this.messages.length;
	}

	constructor(
		private rasaResponceService: GetRasaResponceService, 
		private btnManagerService: ButtonManagerService,
		private atmLocationCardService: AtmLocationCardsService
		) { }
}
