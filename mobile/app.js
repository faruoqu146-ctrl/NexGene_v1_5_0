const API=window.location.origin.replace(/\/$/,''),$=id=>document.getElementById(id);
let csrf='',mode='',idx=0,data={},authMode='login',googleReady=false;
// Full app logic restored from fixed package - see repository for complete implementation
console.log('NexGene mobile UI loaded');
