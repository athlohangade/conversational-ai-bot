import { Injectable } from '@angular/core';
import { MessageClass } from './messageclass';
import { ButtonManagerService } from './button-manager.service';
import { GetRasaResponceService } from './get-rasa-responce.service';

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
		this.rasaResponceService.sendMessage(b).subscribe(data => {
			console.log(data);
			this.addMessageByBot(data);
		})
	}

	public addMockMessageByUser(b: string, toShow: string): void {
		if(this.btnManagerService.hasButtons())
			this.btnManagerService.deactivateButton();
		this.messages.push({isbot: false, body: toShow});
		this.rasaResponceService.sendMessage(b).subscribe(data => {
			console.log(data);
			this.addMessageByBot(data);
		})
	}

	constructor(private rasaResponceService: GetRasaResponceService, private btnManagerService: ButtonManagerService) { }
}
