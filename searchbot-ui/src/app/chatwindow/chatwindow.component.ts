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

	@Input() height: number = 400;
	@Input() width: number = 450;

	@ViewChild('mainchatscreen') private mainchatscreen: ElementRef;
	@ViewChild('inputfield') private inputfield: ElementRef;

	public chatheight: number;
	public chatwidth: number;
	public textboxwidth: number;
	public actwidth: string;
	public actheight: string;

	public hide: boolean = false;
	public fullscreen: boolean = false;
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
		this.setHeightWidth();
	}

	private setHeightWidth() {
		if(!this.fullscreen) {
			this.actheight = `${this.height}px`;
			this.actwidth = `${this.width}px`;
		}
		else {
			this.actheight = `70vh`;
			this.actwidth = `100vw`;
		}
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
		if(this.fullscreen)
			this.changeWindowSize();
		this.hide = !this.hide;
		if(this.hide)
			this.btnsign = "O";
		else
			this.btnsign = "X";
	}

	scrollDown(): void {
		this.mainchatscreen.nativeElement.scrollTop = this.mainchatscreen.nativeElement.scrollHeight;
	}

	resetTextArea(): void {
		this.textboxval = "";
	}

	changeWindowSize(): void {
		this.fullscreen = !this.fullscreen;
		this.setHeightWidth();
	}

	ngOnInit(): void {
		document.onblur = () => this.hasFocus = false;
		document.onfocus = () => this.hasFocus = true;
		window.onblur = () => this.hasFocus = false;
		window.onfocus = () => this.hasFocus = true;
		this.messages.addMessageByBot([{"text": "Hello! I am a bot here to assist you..."}, {"text": "How can I help you?"}]);
	}

	focusOnInput(): void {
		this.inputfield.nativeElement.focus();
	}

	ngAfterViewChecked(): void {
		var num: number;
		if(!this.hide) {
			this.scrollDown();
		}
		if(this.hasFocus) 
			this.count = this.messages.totalMessages();
		else {
			num = this.messages.totalMessages();
			if(this.count < num) 
				this.notification.play();
		}
	}

}
