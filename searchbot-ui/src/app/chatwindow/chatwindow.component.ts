import { Component, OnInit } from '@angular/core';
import { AllmessagesService } from '../allmessages.service';
import { GetRasaResponceService } from '../get-rasa-responce.service';

@Component({
  selector: 'app-chatwindow',
  templateUrl: './chatwindow.component.html',
  styleUrls: ['./chatwindow.component.css']
})
export class ChatwindowComponent implements OnInit {

	constructor(public messages: AllmessagesService, private rasaResponceService: GetRasaResponceService) { }

	sendMessage(m: string): void {
		this.messages.addMessage("usermessage", "user.jpg", m)
		this.rasaResponceService.sendMessage(m).subscribe(data => {
			console.log(data);
			this.messages.addMessage("botmessage", "bot.jpg", data[0].text);
		})
	}

	ngOnInit(): void {
	}

}
