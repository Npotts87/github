var eeyore = {character: "Eeyore", greet: function(){console.log("Thanks for noticin' me");}};
var heffalumps = {character: "Heffalups", greet: function(){console.log("Heffalumps is a marvelous place!");}};
var kanga = {character: "Kanga", greet: function(){console.log("Do be careful, dear!");}};
var christopher = {character: "Christopher", greet: function(){console.log("Welcome to my home!");}};
var pooh = {character: "Pooh", greet: function(){console.log("I am short, fat, and proud of that.");}};
var tigger = {character: "Tigger", greet: function(){console.log("The wonderful thing about Tiggers is Tiggers are wonderful things!");}};
var owl = { character: "Owl", greet: function(){console.log("Artistic talent runs through my family. In fact, it practically stampedes");}};
var piglet = {character: "Piglet", greet: function(){console.log("A giggle a day keeps the blues away” quotes!");}};
var rabbit = {character: "Rabbit", greet: function(){console.log("If there ever comes a day when we can't be together, keep me in your heart, I'll stay there forever");}};
var gopher = {character: "Gopher", greet: function(){console.log("Well, I can't shhhh-tand around lollygaggin' all day.");}};
var bees = {character: "Bees", greet: function(){console.log("Beeeeeeeezzzzzzzzzzzzzz");}};

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

function move(direction) {
    if (player.location[direction] === undefined) {
        return "You cannot go " + direction;
    }else {
        player.location = player.location[direction];
        console.log("You are now at " + player.location.character + "house");
        player.location.greet();
    }
}

console.log(move("north"));
console.log(move("north"));
console.log(move("east"));
console.log(move("east"));
console.log(move("east"));

