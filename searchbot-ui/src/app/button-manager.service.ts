import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ButtonManagerService {

	private isButtonActivated: boolean = false;

	btn: object = null;

	public hasButtons(): boolean {
		return this.isButtonActivated;
	}

	public activateButton(btn: object): void {
		this.isButtonActivated = true;
		this.btn = btn;
	}

	public deactivateButton(): void {
		this.isButtonActivated = false;
	}

	constructor() { }
}
