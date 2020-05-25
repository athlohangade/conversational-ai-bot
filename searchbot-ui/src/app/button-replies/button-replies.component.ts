import { Component, OnInit, Input } from '@angular/core';
import { AllmessagesService } from '../allmessages.service';

@Component({
  selector: 'app-button-replies',
  templateUrl: './button-replies.component.html',
  styleUrls: ['./button-replies.component.css']
})
export class ButtonRepliesComponent implements OnInit {

	@Input() btn: object;
	@Input() viewmore: boolean = false;

	constructor(private messages: AllmessagesService) { }

	sendMessage(message: string, mockMessage: string): void {
		this.messages.addMockMessageByUser(message, mockMessage);
		if(this.viewmore)
			this.showMoreATMCards();
	}

	showMoreATMCards(): void {

	}

	ngOnInit(): void {
	}

}
