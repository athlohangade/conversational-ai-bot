import { Component, OnInit } from '@angular/core';
import { AllmessagesService } from '../allmessages.service';
import { GetRasaResponceService } from '../get-rasa-responce.service';
import { MessageboxComponent } from '../messagebox/messagebox.component';

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
		var link: string = "";
		var strings: string[];
		var m: string = this.textboxval.trim();
		this.textboxval = "";
		if(m == "")
			return;
		this.messages.addMessage(false, m);
		this.rasaResponceService.sendMessage(m).subscribe(data => {
			console.log(data);
			this.messages.addMessage(true, data)
		})
	}

	resetTextArea():void {
		this.textboxval = "";
	}

	ngOnInit(): void {
	}

}
