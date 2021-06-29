using System.Collections.Generic;
using ExtRamp.core;
using ExtRamp.data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Newtonsoft.Json;

namespace ExtRamp.Pages
{
    public class APIModel : PageModel
    {
        public IActionResult OnGet()
        {
            return RedirectToPage("./Index");
        }

        private readonly IRampData rampData;

        public APIModel (IRampData rampData)
        {
            this.rampData = rampData;
        }

        public IEnumerable<Ramp> Ramps { get; set; }

        /*
        public void OnGet()
        {
            Ramps = rampData.GetAllRamps();
        }
        */
    }
}