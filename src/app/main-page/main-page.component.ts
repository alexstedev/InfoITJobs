import { Component, ViewContainerRef } from '@angular/core';
import { ApplyModalComponent } from '../start-modal/apply-modal.component';
import { NovoModalService } from 'novo-elements';



@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
})
export class MainPageComponent {

  public filterCount: number = 1;
  public listFilter: any = {};
  public displaySidebar: boolean = false;
  public loading: boolean = true;
  public error: boolean = false;
  public sidebarCss: object = {};


  constructor(
    private modalService: NovoModalService,
    private viewContainerRef: ViewContainerRef,
  ) {
    // this.modalService.parentViewContainer = this.viewContainerRef;
    this.modalService.open(ApplyModalComponent, {
      job: "IT",
      source: "TEST1",
      viewContainer: this.viewContainerRef,
    }).onClosed.then();
  }

  public onSidebarFilter(filter: any): void {
    this.listFilter = filter;
    this.filterCount++;
  }

  public toggleSidebar(value: boolean): void {
    this.displaySidebar = value;
    if (value) {
      this.sidebarCss = {
        position: 'absolute',
        width: '60%',
        'max-width': 'unset',
      };
    } else {
      this.sidebarCss = {};
    }
  }

  public handleListLoad(loading: boolean): void {
    this.loading = loading;
  }

  public handleError(showError: boolean): void {
    this.error = showError;
  }

}
