#!/bin/bash

numErrors=0

if ! diff -q test/ICS_GOOD_11.html test/ICS_TEST_11.html; then
    echo "ICS_GOOD_11.html does not match ICS_TEST_11.html"
    numErrors=$((numErrors+1))
fi

if ! diff -q test/ICS_GOOD_12.html test/ICS_TEST_12.html; then
    echo "ICS_GOOD_12.html does not match ICS_TEST_12.html"
    numErrors=$((numErrors+1))
fi

if ! diff -q test/ICS_GOOD_13.html test/ICS_TEST_13.html; then
    echo "ICS_GOOD_13.html does not match ICS_TEST_13.html"
    numErrors=$((numErrors+1))
fi

if ! diff -q test/VAlarm_good.html test/VAlarm_test.html; then
    echo "VAlarm_good.html does not match VAlarm_test.html"
    numErrors=$((numErrors+1))
fi

if ! diff -q test/ideal_good.html test/ideal_test.html; then
    echo "ideal_good.html does not match ideal_test.html"
    numErrors=$((numErrors+1))
fi

echo "-----------------------------------------"
echo "Test suite complete with $numErrors errors"
echo "-----------------------------------------"
