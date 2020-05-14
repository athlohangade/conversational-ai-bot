import { Component, OnInit, Input } from '@angular/core';
import { ButtonManagerService } from '../button-manager.service';

@Component({
  selector: 'app-button-replies',
  templateUrl: './button-replies.component.html',
  styleUrls: ['./button-replies.component.css']
})
export class ButtonRepliesComponent implements OnInit {

	@Input() btn: object;

	constructor(public btnManagerService: ButtonManagerService) { }

	ngOnInit(): void {
	}

}
