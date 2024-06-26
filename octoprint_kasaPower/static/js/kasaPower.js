/*
 * View model for OctoPrint-Kasapower
 *
 * Author: chipepper
 * License: AGPLv3
 */


$(function() {
    function KasapowerViewModel(parameters) {
        var self = this;
		


        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];
	

	this.testCommand = function() {
		console.log('button is pressed!')
	};

        this.sendCommand = function () {
            $.ajax({
                url: API_BASEURL + "plugin/kasaPower",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({
			command: "powerOn"
                }),
                contentType: "application/json; charset=UTF-8",

                success: function (data, status, foo) {
			console.log('SUCCESS!');
			console.log(data['switchOn']);
			if(data['switchOn']){
	                        document.getElementById("powerLoading").style.display = 'none';
				document.getElementById("powerOff").style.display = 'none';
			}else{
        	                document.getElementById("powerLoading").style.display = 'none';
				document.getElementById("powerOff").style.display = 'block';
			}
		}
            });
        };
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: KasapowerViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: ["loginStateViewModel", "settingsViewModel"],
        // Elements to bind to, e.g. #settings_plugin_kasaPower, #tab_plugin_kasaPower, ...
        elements: ["#navbar_plugin_kasaPower"]
    });
});
