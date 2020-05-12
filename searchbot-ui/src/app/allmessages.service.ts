import { Injectable } from '@angular/core';
import { MessageClass } from './messageclass';

@Injectable({
  providedIn: 'root'
})
export class AllmessagesService {

	messages: MessageClass[] = [];
	
	addMessage(t: boolean, b: any): void {
		this.messages.push({isbot: t, body: b});
	}

	constructor() { }
}
