import { Injectable } from '@angular/core';
import { MessageClass } from './messageclass';
import { ButtonManagerService } from './button-manager.service';

@Injectable({
  providedIn: 'root'
})
export class AllmessagesService {

	messages: MessageClass[] = [];
	
	public addMessageByBot(b: object[]): void {
		for(let data of b) 
			if(data.hasOwnProperty('buttons')) {
				this.btnManagerService.activateButton(data);
				break;	
			}
		this.messages.push({isbot: true, body: b});
	}

	public addMessageByUser(b: string) {
		this.messages.push({isbot: false, body: b});
	}

	constructor(private btnManagerService: ButtonManagerService) { }
}
