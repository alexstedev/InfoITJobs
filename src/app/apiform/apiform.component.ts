// app.component.ts
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { Router } from '@angular/router';
@Component({
  selector: 'app-api-form',
  templateUrl: './apiform.component.html',
  styleUrls: ['./apiform.component.scss']
})
export class APIFormComponent {

  constructor(private router: Router) { }


  profileForm = new FormGroup({
    skill1: new FormControl(false),
    skill2: new FormControl(false),
    skill3: new FormControl(false),
    skill4: new FormControl(false),
    skill5: new FormControl(false),
    skill6: new FormControl(false),
    skill7: new FormControl(false),
    skill8: new FormControl(false),
    skill9: new FormControl(false),
  });
  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.profileForm.value);
    this.router.navigate(['jobs']);
  }
}