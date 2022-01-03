document.addEventListener("gotoHeader", () => {
    document.querySelector(".header").scrollIntoView({behavior: "smooth",block: "start"});
    
});
document.addEventListener("gotoProgram", () => {
    document.querySelector(".program-gaban").scrollIntoView({behavior: "smooth",block: "start"});
    
});

document.addEventListener("gotoSponsor", () => {
    document.querySelector(".title-sponsor").scrollIntoView({behavior: "smooth",block: "start"});
    
});

document.addEventListener("gotoFooter", () => {
    document.querySelector(".footer").scrollIntoView({behavior: "smooth",block: "start"});
    
});
