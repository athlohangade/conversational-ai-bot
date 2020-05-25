import { Component, Input, OnInit } from '@angular/core';

import { LocationCardComponent } from '../location-card/location-card.component';

@Component({
  selector: 'app-messagebox',
  templateUrl: './messagebox.component.html',
  styleUrls: ['./messagebox.component.css']
})
export class MessageboxComponent implements OnInit {

	@Input() isbot: boolean;
	@Input() body: any;

	public userDisplayPicture = "assets/images/user.png";
	public botDisplayPicture = "assets/images/mastercard-logo.jpg";

	constructor() { }

	ngOnInit(): void {
		var data2: any[] = [];
		var atmcards: any[] = [];
		if(this.isbot) {
			for(let data of this.body) {
				if(data.hasOwnProperty("custom"))
					atmcards.push(data.custom);
				else {
					if(atmcards.length > 0) {
						data2.push({'cards': atmcards});
						atmcards = []
					}
					data2.push(data);
				}
			}
			if(atmcards.length > 0)
				data2.push({'cards': atmcards});
			this.body = data2;
		}
	}

}
