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
	
	private addMessageByBot(b: any[]): void {
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
				console.log(data);
				this.addMessageByBot(data);
			}
		);
	}

	public addMockMessageByUser(b: string, toShow: string): void {
		if(this.btnManagerService.hasButtons())
			this.btnManagerService.deactivateButton();
		this.messages.push({isbot: false, body: toShow});
		this.rasaResponceService.sendMessage(b).pipe(
			catchError(
				(error: HttpErrorResponse) => {
					console.log("Upps:", error);
					this.addMessageByBot([{text: "Sorry, I can not reach to server right now. Please check your internet connectivity and try again :("}]);
					return EMPTY;
				}
			)
		)
		.subscribe(
			(data: any) => {
				console.log(data);
				this.addMessageByBot(data);
			}
		);
	}

	constructor(private rasaResponceService: GetRasaResponceService, private btnManagerService: ButtonManagerService) { }
}
