import { ComponentFixture, TestBed } from '@angular/core/testing';

import { APIFormComponent } from './apiform.component';

describe('APIFormComponent', () => {
  let component: APIFormComponent;
  let fixture: ComponentFixture<APIFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ APIFormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(APIFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
