import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ButtonRepliesComponent } from './button-replies.component';

describe('ButtonRepliesComponent', () => {
  let component: ButtonRepliesComponent;
  let fixture: ComponentFixture<ButtonRepliesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ButtonRepliesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ButtonRepliesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
