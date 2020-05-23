import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import { AllmessagesService } from '../allmessages.service';
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
	@ViewChild('inputfield') private inputfield: ElementRef;

	public chatheight: number;
	public chatwidth: number;
	public textboxwidth: number;

	public hide: boolean = false;
	public btnsign: string = "X";

	private hasFocus: boolean = true;
	private count: number = 0;
	private notification: HTMLAudioElement;

	textboxval: string = "";

	constructor(public messages: AllmessagesService, public btnManagerService: ButtonManagerService) { 
		this.chatheight = this.height - 50;
		this.chatwidth = this.width - 35;
		this.textboxwidth = this.width - 40;
		this.notification = new Audio('assets/sounds/definite.mp3');
	}

	/* only use when testing, shows some messages at the start
	 * session to check the look 
	 */
	async testMessages() {
		this.sendMessage("hi");
		this.sendMessage("how are you?");
	}

	sendMessage(m: string): void {
		if(m == "")
			return;
		this.count++;
		this.messages.addMessageByUser(m);		
	}

	sendMessageInTextArea(): void {
		var m: string = this.textboxval.trim();
		this.textboxval = "";
		this.sendMessage(m);
	}

	hideChat(): void {
		this.hide = !this.hide;
		if(this.hide)
			this.btnsign = "O";
		else
			this.btnsign = "X";
	}

	scrollDown(): void {
		this.mainchatscreen.nativeElement.scrollTop = this.mainchatscreen.nativeElement.scrollHeight;
	}

	resetTextArea():void {
		this.textboxval = "";
	}

	ngOnInit(): void {
		document.onblur = () => {this.hasFocus = false; console.log("BLURRED");}
		document.onfocus = () => this.hasFocus = true;
		window.onblur = () => {this.hasFocus = false; console.log("BLURRED");}
		window.onfocus = () => this.hasFocus = true;
		this.messages.addMessageByBot([{"text": "Hello! I am a bot here to assist you..."}, {"text": "How can I help you?"}]);
	}

	ngAfterViewChecked(): void {
		var num: number;
		console.log("CHECKED");
		if(!this.hide) {
			this.scrollDown();
			this.inputfield.nativeElement.focus();
		}
		if(this.hasFocus) 
			this.count = this.messages.totalMessages();
		else {
			console.log("PLAYING AUDIO");
			num = this.messages.totalMessages();
			if(this.count < num) 
				this.notification.play();
		}
	}

}
