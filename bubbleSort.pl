#!/usr/bin/perl

use strict;
use warnings;

sub bubbleSort{
        print "Unsorted list:  @_ \n";
        my $swap=1; #swap is true / sorted

        while($swap){
                $swap = 0; #swap is false / unsorted
                for(my $i = 1; $i < @_; $i++){
                        if($_[$i] < $_[$i-1]){
                                $swap=1;
                                @_[$i,$i-1]=@_[$i-1,$i];
                        }
                }
        }
        return @_;
}

my @arr = (10,-34,119,0,22,190,10500,-22,-65,-1);
bubbleSort(@arr);
print "Sorted list: @arr \n";
