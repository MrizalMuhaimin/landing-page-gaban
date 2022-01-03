const program_header_btn = document.getElementsByClassName("program-header");
const berita_header_btn = document.getElementsByClassName("berita-header");
const tentang_kami_header_btn = document.getElementsByClassName("tentang-kami-header");

program_header_btn[0].onclick = function() {
    document.querySelector(".program-gaban").scrollIntoView({behavior: "smooth",block: "start"});
}

berita_header_btn[0].onclick = function() {
    document.querySelector(".title-sponsor").scrollIntoView({behavior: "smooth",block: "start"});
}

tentang_kami_header_btn[0].onclick = function() {
    document.querySelector("footer").scrollIntoView({behavior: "smooth",block: "start"});
}
