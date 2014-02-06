angular.module('pantestingApp').controller('Hosts',
  function($scope, $rootScope) {
        $scope.hosts = [{name: 'My Host', time_left: '1 week', company: 'My company 1'},
                        {name: 'PayPal.com', time_left: '24 hours', company: 'PayPal'}]

        $scope.openHost = function(host) {
            $scope.$parent.currentView = 'details';
        }
  });

angular.module('pantestingApp').controller('HostDetails',
  function($scope, $routeParams) {
        $scope.hostId = $routeParams.hostId;
  });