import { Injectable } from '@angular/core';
import { MessageClass } from './messageclass';
import { ButtonManagerService } from './button-manager.service';
import { GetRasaResponceService } from './get-rasa-responce.service';
import { catchError } from 'rxjs/operators';
import { HttpErrorResponse } from '@angular/common/http'; 
import { EMPTY } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AllmessagesService {

	messages: MessageClass[] = [];
	
	public addMessageByBot(b: any[]): void {
		for(let data of b) 
			if(data.hasOwnProperty('buttons')) {
				this.btnManagerService.activateButton(data.buttons);
				break;	
			}
		this.messages.push({isbot: true, body: b});
	}

	public addMessageByUser(b: string):void {
		if(this.btnManagerService.hasButtons())
			this.btnManagerService.deactivateButton();
		this.messages.push({isbot: false, body: b});
		this.rasaResponceService.sendMessage(b).pipe(
			catchError(
				(error: HttpErrorResponse) => {
					console.log(error);
					this.addMessageByBot([{text: "Sorry, I can not reach to server right now. Please check your internet connectivity and try again :("}]);
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
						this.addMessageByBot([{text: "Sorry, I can not reach to server right now. Please check your internet connectivity and try again :("}]);
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

	constructor(private rasaResponceService: GetRasaResponceService, private btnManagerService: ButtonManagerService) { }
}
