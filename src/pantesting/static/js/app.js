var pantestingApp = angular.module('pantestingApp', ['ngRoute', 'pantestServices']);

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
            .when('/register', {
				templateUrl : 'static/html/registration.html',
				controller  : 'HostDetails'
			})
            .when('/profile', {
				templateUrl : 'static/html/profile.html',
				controller  : 'Profile'
			})


	}]).run(function($rootScope, $location){
    $rootScope.$on("$routeChangeStart", function(event, currRoute, prevRoute) {
            if(currRoute.requiresLogin && !$rootScope.isAuthenticated()) {
                alert('Login required');
                $location.path("/");
            }
    });
});

var phonecatServices = angular.module('pantestServices', ['ngResource']);

pantestingApp.factory('Host', ['$resource',
  function($resource){
    return $resource('get_hosts/:hostId', {}, {
      query: {method:'GET', params: {hostId:'all'}   }
    });
  }]);