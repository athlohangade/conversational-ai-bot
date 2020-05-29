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

	public messages: MessageClass[] = [];

	public botPendingMessages: number = 1;
	
	public addMessageByBot(b: any[]): void {
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
		if(this.botPendingMessages > 0)
			this.botPendingMessages--;
	}

	public show4(): void {
		if(this.botPendingMessages > 0)
			this.botPendingMessages--;
		var cards = this.atmLocationCardService.pop4();
		var cardobject: any[] = [];
		for(let card of cards)
			cardobject.push({'custom': card});
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
		this.GetRasaResponseFor(b);
	}

	public addMockMessageByUser(b: string, toShow: string): void {
		if(this.btnManagerService.hasButtons())
			this.btnManagerService.deactivateButton();
		this.messages.push({isbot: false, body: toShow});
		this.GetRasaResponseFor(b);
	}

	private GetRasaResponseFor(b: string) {
		this.botPendingMessages++;
		if (b != null) {
			this.rasaResponceService.sendMessage(b)
			.pipe(catchError((error: HttpErrorResponse) => {
				console.log(error);
				this.addMessageByBot([{
					text: "Sorry, I can not reach to server right now. \
						Please check your internet connectivity and try again :("
				}]);
				return EMPTY;
			}))
			.subscribe((data: any) => {
				this.addMessageByBot(data);
			});
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
