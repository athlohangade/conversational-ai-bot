import { Injectable } from '@angular/core';
import { MessageClass } from './messageclass';

@Injectable({
  providedIn: 'root'
})
export class AllmessagesService {

	messages: MessageClass[] = [];
	
	addMessage(t: string, s: string, b: string): void {
		this.messages.push({mtype: t, source: s, body: b});
	}

	constructor() { }
}
