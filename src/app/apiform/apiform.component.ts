// app.component.ts
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
	selector: 'app-api-form',
	templateUrl: './apiform.component.html',
	styleUrls: ['./apiform.component.scss']
})
export class APIFormComponent implements OnInit {
	customerForm: FormGroup;
	customer: any;
	message: string;
	constructor(private formBuilder: FormBuilder) { }

	ngOnInit() {
		this.customer = {
			firstName: 'Tina Reactive'
		};

		this.customerForm = this.formBuilder.group({
			firstName: [this.customer.firstName, Validators.required]
		});
	}

	onSubmit(form: FormGroup) {
		this.message = 'You typed: ' + form.controls.firstName.value;
	}

}
