var pantestingApp = angular.module('pantestingApp', ['ngRoute']);

pantestingApp.config(['$routeProvider', function($routeProvider) {
		$routeProvider
			.when('/', {
				templateUrl : 'static/html/search.html',
				controller  : 'Hosts'
			})
			.when('/host/:hostId', {
				templateUrl : 'static/html/details.html',
				controller  : 'HostDetails'
			})
            .when('/new_host', {
				templateUrl : 'static/html/details.html',
				controller  : 'HostDetails',
                requiresLogin: true
			})


	}]).run(function($rootScope, $location){
    $rootScope.$on("$routeChangeStart", function(event, currRoute, prevRoute) {
            if(currRoute.requiresLogin && !$rootScope.isAuthenticated()) {
                alert('Login required');
                $location.path("/");
            }
    });
});