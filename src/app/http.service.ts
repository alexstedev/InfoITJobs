import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
	providedIn: 'root'
})
export class HttpService {

	private url = 'http://127.0.0.1:8000/';
	constructor(private http: HttpClient) { }

	getOffers(page?: number, subcategory?: string) {
		_query = this.url + 'offers?';

		if (typeof subcategory !== "undefined") {
			if (typeof page !== "undefined") {
				_query += 'page=' + (page as string) + '&subcategory=' + subcategory;
			}
			else {
				_query += 'subcategory=' + subcategory;
			}
		}
		else {
			_query += 'page=' + (page as string);
		}

		return this.http.get(_query);
	}

	getCategories() {
		_query = this.url + 'condensed_categories';
		return this.http.get(_query);
	}

}
