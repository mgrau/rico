var plantations = [2,6,1,4,0,0,2,0,2,0,0,0];
var building = [0,0,0,0,0,0,0,0,0,0,0,0];

$(document).ready(function() {
    $('body').append('<div id="player"></div>');
    $('#player').append('<div id="island"></div>');
    $('#island').append('<div id="plantations"></div>');
    $('#island').append('<div id="buildings"></div>');
    for (i=0;i<12;i++)
    {
        $('#plantations').append('<div></div>');
    }
    $('#plantations > div').addClass("plantation");
    $('.plantation').each(function(index,plantation) {
        draw_plantation(plantation,plantations[index],(index%3)*80,((index-index%3)/3)*80)
    });

    for (i=0;i<12;i++)
    {
        $('#buildings').append('<div></div>');
    }
    $('#buildings > div').addClass("building");
    $('.building').each(function(index, building) {
        $(building).addClass("small-market");
        $(building).css("left", (index%4)*125);
        $(building).css("top", ((index-index%4)/4)*70);
        $(building).html('<div>Small Market</div>');
        $(building).click(function(){
            alert('You have click building '+index);
        });
    });
});

function draw_plantation(plantation, type, left_pos, top_pos)
{
    if (type==1) {
        $(plantation).addClass("corn"); }
    else if (type==2) {
        $(plantation).addClass("indigo");
        $(plantation).append('<div class="circle"></div>');
        $(plantation).children('.circle').css('top',47);
        $(plantation).children('.circle').css('left',47);
        }
    else if (type==3) {
        $(plantation).addClass("sugar"); }
    else if (type==4) {
        $(plantation).addClass("tobacco"); }
    else if (type==5) {
        $(plantation).addClass("coffee"); }
    else if (type==6) {
        $(plantation).addClass("quarry"); }
    $(plantation).css("left", left_pos);
    $(plantation).css("top", top_pos);
}