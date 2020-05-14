import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import { AllmessagesService } from '../allmessages.service';
import { GetRasaResponceService } from '../get-rasa-responce.service';
import { MessageboxComponent } from '../messagebox/messagebox.component';
import { ButtonManagerService } from '../button-manager.service';
import { ButtonRepliesComponent } from '../button-replies/button-replies.component';

@Component({
  selector: 'app-chatwindow',
  templateUrl: './chatwindow.component.html',
  styleUrls: ['./chatwindow.component.css']
})
export class ChatwindowComponent implements OnInit {

	@Input() height: number = 800;
	@Input() width: number = 500;

	@ViewChild('mainchatscreen') private mainchatscreen: ElementRef;

	public chatheight: number;
	public chatwidth: number;
	public textboxwidth: number;

	public hide: boolean = true;

	textboxval: string = "";

	constructor(public messages: AllmessagesService, private rasaResponceService: GetRasaResponceService, private btnManagerService: ButtonManagerService) { 
		this.chatheight = this.height - 50;
		this.chatwidth = this.width - 35;
		this.textboxwidth = this.width - 40;
	}

	/* only use when testing, shows some messages at the start
	 * session to check the look 
	 */
	async testMessages() {
		this.textboxval = "hi";
		this.sendMessage();
		this.textboxval = "hello";
		this.sendMessage();
	}

	sendMessage(m: string): void {
		if(this.btnManagerService.hasButtons())
			this.btnManagerService.deactivateButton();
		this.textboxval = "";
		if(m == "")
			return;
		this.messages.addMessageByUser(m);
		this.rasaResponceService.sendMessage(m).subscribe(data => {
			console.log(data);
			this.messages.addMessageByBot(data)
		})
	}

	sendMessageInTextArea(): void {
		var m: string = this.textboxval.trim();
		this.sendMessage(m);
	}

	hideChat(): void {
		this.hide = !this.hide;
	}

	scrollDown(): void {
		this.mainchatscreen.nativeElement.scrollTop = this.mainchatscreen.nativeElement.scrollHeight;
	}

	resetTextArea():void {
		this.textboxval = "";
	}

	ngOnInit(): void {
	}

}
