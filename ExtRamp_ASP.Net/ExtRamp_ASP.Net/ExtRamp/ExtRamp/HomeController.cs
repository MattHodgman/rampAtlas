using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace ExtRamp
{
    public class HomeController : Controller
    {
        // GET: /<controller>/
        public IActionResult Index()
        {
            return View();
        }

        public ActionResult DownloadFile(int rand, string uploaded_file, string uploaded_file_tAI, string uploaded_file_rscu)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory + "Output_files/";
            ViewData["path"] = path;
            byte[] fileBytes = System.IO.File.ReadAllBytes(path + "ramp_output_" + rand + ".fasta");
            System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\ramp_output_" + rand + ".fasta");
            System.IO.File.Delete("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file);
            if (uploaded_file_tAI != "none")
                System.IO.File.Delete("C:\\Users\\matthod\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file_tAI);
            if (uploaded_file_rscu != "none")
                System.IO.File.Delete("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file_rscu);
            string fileName = "ramp_output_" + rand + ".fasta";
            return File(fileBytes, System.Net.Mime.MediaTypeNames.Application.Octet, fileName);
        }

        public ActionResult DownloadFile1(string file)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory + "Ramp_percentages/";
            ViewData["path"] = path;
            byte[] fileBytes = System.IO.File.ReadAllBytes(path + file);
            return File(fileBytes, System.Net.Mime.MediaTypeNames.Application.Octet, file);
        }

        public ActionResult DownloadNote(string file)
        {
            string path = "C:\\Users\\matthodg\\";
            ViewData["path"] = path;
            byte[] fileBytes = System.IO.File.ReadAllBytes(path + file);
            System.IO.File.Delete("C:\\Users\\matthodg\\" + file);
            return File(fileBytes, System.Net.Mime.MediaTypeNames.Application.Octet, file);
        }
    }
}
