import { Component, OnInit } from '@angular/core';
import { AllmessagesService } from '../allmessages.service';
import { GetRasaResponceService } from '../get-rasa-responce.service';

@Component({
  selector: 'app-chatwindow',
  templateUrl: './chatwindow.component.html',
  styleUrls: ['./chatwindow.component.css']
})
export class ChatwindowComponent implements OnInit {

	textboxval: string = "";

	constructor(public messages: AllmessagesService, private rasaResponceService: GetRasaResponceService) { }

	sendMessage(): void {
		var messageToShow: string = "";
		var strings: string[];
		var m: string = this.textboxval;
		this.textboxval = "";
		this.messages.addMessage("usermessage", "user.jpg", m)
		this.rasaResponceService.sendMessage(m).subscribe(data => {
			console.log(data);
			strings = data.map(obj => obj.text);
			messageToShow = strings.join("\n");
			this.messages.addMessage("botmessage", "bot.jpg", messageToShow);
		})
	}

	ngOnInit(): void {
	}

}
