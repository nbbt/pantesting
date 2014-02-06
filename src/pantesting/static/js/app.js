var pantestingApp = angular.module('pantestingApp', ['ngRoute']);

pantestingApp.config(['$routeProvider', function($routeProvider) {
		$routeProvider

			// route for the home page
			.when('/', {
				templateUrl : 'static/html/search.html',
				controller  : 'Hosts'
			})

			// route for the about page
			.when('/host/:hostId', {
				templateUrl : 'static/html/details.html',
				controller  : 'HostDetails'
			})

	}]);