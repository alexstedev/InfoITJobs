import { Component } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';

@Component({
    selector: 'start-form',
    templateUrl: './start-form.component.html',
    styleUrls: ['./start-form.component.css']
})
export class ModalFormComponent {
    validatingForm: FormGroup;

    constructor() {
        this.validatingForm = new FormGroup({
            contactFormModalName: new FormControl('', Validators.required),
            contactFormModalEmail: new FormControl('', Validators.email),
            contactFormModalSubject: new FormControl('', Validators.required),
            contactFormModalMessage: new FormControl('', Validators.required)
        });
    }

    get contactFormModalName() {
        return this.validatingForm.get('contactFormModalName');
    }

    get contactFormModalEmail() {
        return this.validatingForm.get('contactFormModalEmail');
    }

    get contactFormModalSubject() {
        return this.validatingForm.get('contactFormModalSubject');
    }

    get contactFormModalMessage() {
        return this.validatingForm.get('contactFormModalMessage');
    }
}