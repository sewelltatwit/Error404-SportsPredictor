function displayText() {
        
        var ddlTeamOne = document.getElementById("ddlFirstTeam");
        var teamOne = ddlTeamOne.options(ddlTeamOne.selectedIndex).value;
        var ddlTeamTwo = document.getElementById("ddlTeamTwo");
        var teamTwo = ddlTeamTwo.options(ddlTeamTwo.selectedIndex).value;
        $.getJSON(
            '/finalResult' + '/' + teamOne + '/' + teamTwo,
            function (data) {
            
            
        });
}

function clear() {
    document.getElementById("btnResult").innerHTML='';
    document.getElementById("ddlFirstTeam").selectedIndex = 1;
}

