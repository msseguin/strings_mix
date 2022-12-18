
#!/bin/bash
amort() {
    balance=${2}
    term=${3}
    numPayment=${4}
    yearlyRate=${1}

    echo "${yearlyRate}/(100*12)"

    monthIntR=`echo "${1}/(100.0*12.0)" | bc -l`

    echo "(${monthIntR} * ${balance}) / (1- (1 + ${monthIntR})**-${term})"
    numerator=`echo "(${monthIntR}*${balance})" | bc -l`
    denom=`echo "(1-(1+${monthIntR})^(-${term}))" | bc -l`
    echo "${denom}"

    monthPay=`echo "(${monthIntR}*${balance})/(1-(1+${monthIntR})^-${term})" | bc -l`

    echo "${monthPay}"

    # using a simple loop to caclulate the principal
    for i in {1..$numPayment}
    do
        int=`echo "${monthIntR}*${balance}" | bc -l`
        echo "${int}"
        # current values
        newBalance=`echo "${balance}-${monthPay}+${int}" | bc -l`
        echo "${newBalance}"
        principal=`echo "${balance}-${newBalance}" | bc -l`
        echo "${principal}"
        interest=$(( monthPay - principal ))

        #carry new balance forward
        balance=$newBalance
        
    done

    echo  "num_payment ${numPayment} c ${monthPay} princ ${principal} int ${interest} balance ${newBalance}"

}
amort $1 $2 $3 $4
