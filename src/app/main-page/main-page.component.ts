import { Component, OnInit, ViewContainerRef } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { SearchService } from '../services/search/search.service';
import { NovoModalService } from 'novo-elements';
import { SettingsService } from '../services/settings/settings.service';
import { AnalyticsService } from '../services/analytics/analytics.service';
import { StartModalComponent } from '../start-modal/start-modal.component';
import { ShareService } from '../services/share/share.service';
import { Title, Meta } from '@angular/platform-browser';
import { JobBoardPost } from '@bullhorn/bullhorn-types';
import { ServerResponseService } from '../services/server-response/server-response.service';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
})
export class MainPageComponent {

  public filterCount: number = 1;
  public listFilter: any = {};
  public displaySidebar: boolean = false;
  public loading: boolean = false;
  public error: boolean = false;
  public sidebarCss: object = {};

  public job: JobBoardPost | any;
  public id: string;
  public source: string;
  public relatedJobs: any;
  public showShareButtons: boolean = false;
  public alreadyApplied: boolean = false;
  public showCategory: boolean = SettingsService.settings.service.showCategory;
  public isSafariAgent: boolean = false;
  private APPLIED_JOBS_KEY: string = 'APPLIED_JOBS_KEY';


  constructor(private service: SearchService,
    private shareService: ShareService,
    private route: ActivatedRoute,
    private router: Router,
    private analytics: AnalyticsService,
    private modalService: NovoModalService,
    private viewContainerRef: ViewContainerRef,
    private titleService: Title,
    private meta: Meta,
    private serverResponse: ServerResponseService,
    private translate: TranslateService,) {

    this.modalService.parentViewContainer = this.viewContainerRef;
    // this.apply()
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

  public apply(): void {
    this.modalService.open(StartModalComponent, {
      viewContainer: this.viewContainerRef,
    });
  }



  public handleListLoad(loading: boolean): void {
    this.loading = loading;
  }

  public handleError(showError: boolean): void {
    this.error = showError;
  }

}
