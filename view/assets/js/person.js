function edit(id) {
    alert("Edit : " + id);
}


async function remove(id) {
    await fetch("/person?id="+id , {
        method: "DELETE"
    })
        .then(response => document.location.replace("/person"));
}