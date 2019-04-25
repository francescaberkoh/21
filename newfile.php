
BlackJack: 


<?php
$dealerfirst_card = mt_rand(1,10);
$dealersecond_card = mt_rand(1,10);
$dealerthird_card  = mt_rand(1,10);

$playerfirst_card = mt_rand(1,10);
$playersecond_card = mt_rand(1,10);


$dealers = $dealerfirst_card + $dealersecond_card + $dealerthird_card;

$players = $playerfirst_card + $playersecond_card ;

echo "You have these cards:" . " " .  $playerfirst_card . " " . $playersecond_card . " ". "Your cards make a combined total of:" . " " .$players;

?>

<form action=""  method="POST">
    <input type="text" name="userinput" placeholder="Hit or Stay"><br>
    <input type="submit" name="check" value="Check">
</form>

<?php
$userinput= $_POST['userinput'];
$checkbutton= $_POST['check'];

if ($checkbutton){
    if($userinput == "hit"){
        $playerthird_card = mt_rand(1,10);
        $current = $playerfirst_card + $playersecond_card +  $playerthird_card ;
        echo "You now have:"." " . $current . " " . "With these cards:" . " " . $playerfirst_card . " " . $playersecond_card . " ". $playerthird_card;
        echo "Dealer now has:" . " " . $dealers . " " . "With these cards:" . " " . $dealerfirst_card . " " . $dealersecond_card . " ". $dealerthird_card;
        
        if ($current <= 21 && $dealers <= 21){
            if($dealers == $current){
                echo "It's a tie!";
            }
            
            if ($current < $dealers){
                echo "Dealer Wins :(";
            }
            if ($current > $dealers){
                echo "You Win!";
            }
        }
        else{
            if ($current > 21){
                echo "You Busted! Dealer Wins :(";
            }
            if ($dealers> 21){
                echo "Dealer Busted! You Win!";
            }
        }

    }


    else{
        echo "Dealer now has:" . " " . $dealers . " " . "With these cards:" . " " . $dealerfirst_card . " " . $dealersecond_card . " ". $dealerthird_card;
        if ($players <= 21 && $dealers <= 21){
            if($dealers == $players){
                echo "It's a tie!";
            }
            
            if ($players < $dealers){
                echo "Dealer Wins :(";
            }
            if ($players > $dealers){
                echo "You Win!";
            }
        }
        else{
            if ($players > 21){
                echo "You Busted! Dealer Wins :(";
            }
            if ($dealers> 21){
                echo "Dealer Busted! You Win!";
            }
        }
    }
}

?>