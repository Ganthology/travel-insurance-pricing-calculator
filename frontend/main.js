// export function handleFormSubmission(e) {
//   e.preventDefault()
//   try {
//     console.log(e)

//   } catch (error) {
//     console.error(error)
//   }
// }

async function testSubmit() {
  const departureDate = document.querySelector('#departure-date').value;
  const returnDate = document.querySelector('#return-date').value;
  const plan = document.querySelector('input[name="plan"]:checked').value;
  const covidAddOn = document.querySelector('#covid-addon').checked;
  const sstApplicable = document.querySelector('#sst').checked;
  const stampDuty = document.querySelector('#stamp-duty').value;

  if (departureDate === '') {
    const message = 'Please select a departure date';
    document.querySelector('#departure-date-error').innerHTML = message;
    return;
  }

  if (returnDate === '') {
    const message = 'Please select a return date';
    document.querySelector('#return-date-error').innerHTML = message;
    return;
  }

  if (plan === '') {
    const message = 'Please select a plan';
    document.querySelector('#plan-error').innerHTML = message;
    return;
  }

  const getPricing = await fetch('http://127.0.0.1:8000/api/pricing-calculator', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      Period: {
        DepartureDate: departureDate,
        ReturnDate: returnDate,
      },
      Plan: +plan,
      CovidAddOn: covidAddOn,
      SST: sstApplicable,
      StampDuty: stampDuty === '' ? undefined : +stampDuty,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.price) {
        document.querySelector('#price').innerHTML = `$ ${data.price}`;
        document.querySelector('#departure-date-error').innerHTML = '';
        document.querySelector('#return-date-error').innerHTML = '';
        document.querySelector('#plan-error').innerHTML = '';
        return;
      } else {
        alert(`Error: ${data.detail[0].msg}`);
      }
    });
}
