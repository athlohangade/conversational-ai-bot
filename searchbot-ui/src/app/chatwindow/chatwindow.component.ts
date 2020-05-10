import { Component, OnInit } from '@angular/core';
import { AllmessagesService } from '../allmessages.service';

@Component({
  selector: 'app-chatwindow',
  templateUrl: './chatwindow.component.html',
  styleUrls: ['./chatwindow.component.css']
})
export class ChatwindowComponent implements OnInit {

	constructor(public messages: AllmessagesService) { }

	sendMessage(m) {
		this.messages.addMessage("usermessage", "user.jpg", m)
	}

	ngOnInit(): void {
	}

}
