var eeyore = {character: "Eeyore", greet: function(){console.log("Thanks for noticin' me");}, honey:false};
var heffalumps = {character: "Heffalups", greet: function(){console.log("Heffalumps is a marvelous place!");}, honey:false};
var kanga = {character: "Kanga", greet: function(){console.log("Do be careful, dear!");}, honey:false};
var christopher = {character: "Christopher", greet: function(){console.log("Welcome to my home!");}, honey:false};
var pooh = {character: "Pooh", greet: function(){console.log("I am short, fat, and proud of that.");}, honey:false};
var tigger = {character: "Tigger", greet: function(){console.log("The wonderful thing about Tiggers is Tiggers are wonderful things!");}, honey:false};
var owl = { character: "Owl", greet: function(){console.log("Artistic talent runs through my family. In fact, it practically stampedes");}, honey:false};
var piglet = {character: "Piglet", greet: function(){console.log("A giggle a day keeps the blues away” quotes!");}, honey:false};
var rabbit = {character: "Rabbit", greet: function(){console.log("If there ever comes a day when we can't be together, keep me in your heart, I'll stay there forever");}, honey:false};
var gopher = {character: "Gopher", greet: function(){console.log("Well, I can't shhhh-tand around lollygaggin' all day.");}, honey:false};
var bees = {character: "Bees", greet: function(){console.log("Beeeeeeeezzzzzzzzzzzzzz");}, honey:false};

heffalumps.west = eeyore;

eeyore.east = heffalumps;
eeyore.south = kanga;

kanga.north = eeyore;
kanga.south = christopher;

christopher.west = owl;
christopher.east = rabbit;
christopher.north = kanga;
christopher.south = pooh;

owl.east = christopher;
owl.south = piglet;

rabbit.west = christopher;
rabbit.east = gopher;
rabbit.south = bees;

gopher.west = rabbit;

pooh.west = piglet;
pooh.north = christopher;
pooh.east = bees;
pooh.south = tigger;

piglet.north = owl;
piglet.east = pooh;

bees.west = pooh;
bees.north = rabbit;

tigger.north = pooh;

var player = {
    location: tigger
}

function pickUp(){
    if (player.location == bees){
        player.honey = true;
        console.log("Yummmm, you've got honey")
    }else{
        console.log("There is no honey at this location")
    }

}
function mission(){
    charList = [tigger, pooh, piglet, christopher, owl, rabbit, gopher, kanga, eeyore, heffalumps]
    var random = Math.floor(Math.random()*Math.floor(charList.length));
    recipient = charList[random];
    recipient.objective = true;
    console.log(recipient.character + " is looking for honey! Can you help?");
}

function drop(){
    if(player.location.objective == true){
        console.log("Congratulations! You delivered honey to " + player.location.character + "!")
    }
    else{
        console.log("Whoops! This isn't the place that needs honey.")
    }
}

function move(direction) {
    if(player.location[direction] === undefined) {
        return "You cannot go " + direction;
    }else{
        player.location = player.location[direction];
        console.log("You are now at " + player.location.character + "house");
        player.location.greet();
        }
    }

console.log(mission);
console.log(move("north"));
console.log(pickUp);

console.log(move("east"));
console.log(pickUp);

console.log(move("east"));
console.log(pickUp);

console.log(move("east"));
console.log(pickUp);

console.log(move("east"));
console.log(pickUp);
console.log(drop);