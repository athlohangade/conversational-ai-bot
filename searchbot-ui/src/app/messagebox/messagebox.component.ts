import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-messagebox',
  templateUrl: './messagebox.component.html',
  styleUrls: ['./messagebox.component.css']
})
export class MessageboxComponent implements OnInit {

	@Input() isbot: boolean;
	@Input() body: object;

	public userDisplayPicture = "assets/images/user.png";
	public botDisplayPicture = "assets/images/bot.png";

	constructor() { }

	ngOnInit(): void {
	}

}
