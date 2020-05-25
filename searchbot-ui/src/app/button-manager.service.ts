import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ButtonManagerService {

	private isButtonActivated: boolean = false;
	private customButton: boolean = false;

	btn: any[] = null;

	public hasButtons(): boolean {
		return this.isButtonActivated;
	}

	public isCustomButton(): boolean {
		return this.customButton;
	}

	public activateButton(btn: any[], customButton: boolean): void {
		this.isButtonActivated = true;
		this.btn = btn;
		this.customButton = customButton;
	}

	public deactivateButton(): void {
		this.isButtonActivated = false;
	}

	constructor() { }
}
