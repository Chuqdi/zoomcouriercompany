window.addEventListener("load", function(){
    let start_tracking_shipment = document.getElementById("start_tracking_shipment");
    let start_tracking_shipment_input = document.getElementById("start_tracking_shipment_input")
    start_tracking_shipment.addEventListener("click", function(e){
      alert("Mififi");
      e.preventDefault();
      let value = start_tracking_shipment_input.value;
      if(value.length < 1){
        alert("Please enter shipment UUID");
        return ;
      }
      let url = "";
      window.open(`/trackShipment/${value}`, "_blank");
      start_tracking_shipment_input.value ="";
    })
  })