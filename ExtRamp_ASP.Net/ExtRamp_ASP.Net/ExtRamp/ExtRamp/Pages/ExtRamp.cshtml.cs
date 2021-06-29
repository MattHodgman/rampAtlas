using System;
using System.IO;
//using System.IO.Compression;
using Ionic.Zip;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Web;
using System.Threading;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Microsoft.AspNetCore.Mvc.DataAnnotations.Internal;

namespace ExtRamp.Pages
{
    public class ExtRampModel : PageModel
    {
        public string Message { get; set; }

        public int Rand;

        public IActionResult OnGet()
        {
            return RedirectToPage("./Index");
        }

        private IHostingEnvironment _environment;
        public ExtRampModel(IHostingEnvironment environment)
        {
            _environment = environment;
        }

        
        [BindProperty]
        public string GeneSequence { get; set; }
        [BindProperty]
        public IFormFile Upload_input { get; set; }
        [BindProperty]
        public IFormFile Upload_tAI { get; set; }
        [BindProperty]
        public IFormFile Upload_rscu { get; set; }
        [BindProperty]
        public bool Vals { get; set; }
        [BindProperty]
        public bool Speeds { get; set; }
        [BindProperty]
        public bool Standard { get; set; }
        [BindProperty]
        public bool AfterRamp { get; set; }
        [BindProperty]
        public bool NoRamps { get; set; }
        [BindProperty]
        public bool RemovedSequences { get; set; }
        [BindProperty]
        public string WhichMean { get; set; }
        [BindProperty]
        public string Tissue { get; set; }
        [BindProperty]
        public int RibosomeWindowLength { get; set; }
        [BindProperty]
        public int BottleNeckLocation { get; set; }
        [BindProperty]
        public int MinSeqLen { get; set; }
        [BindProperty]
        public bool HasRNA { get; set; }
        public string input_file = "none";
        public string tAI_file = "none";
        public string rscu_file = "none";


        public async Task<ActionResult> OnPostAsync()
        {
            // check if input file was uploaded
            if (Upload_input != null)
            {
                var file_input = Path.Combine("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\", Upload_input.FileName);
                using (var fileStream = new FileStream(file_input, FileMode.Create))
                {
                    await Upload_input.CopyToAsync(fileStream);
                }
                input_file = Upload_input.FileName;
            }
            else
            {
                //var file_input = Path.Combine("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\", "example_input.fasta");
                input_file = "example_input.fasta";
            }
            
            bool tAI = false;
            bool rscu = false;

            if (Upload_tAI != null)
            {
                var file_tAI = Path.Combine(_environment.ContentRootPath, "Uploads", Upload_tAI.FileName);
                using (var fileStream = new FileStream(file_tAI, FileMode.Create))
                {
                    await Upload_input.CopyToAsync(fileStream);
                }
                tAI = true;
                tAI_file = Upload_tAI.FileName;
            }

            if (Upload_rscu != null)
            {
                var file_rscu = Path.Combine(_environment.ContentRootPath, "Uploads", Upload_rscu.FileName);
                using (var fileStream = new FileStream(file_rscu, FileMode.Create))
                {
                    await Upload_input.CopyToAsync(fileStream);
                }
                rscu = true;
                rscu_file = Upload_rscu.FileName;
            }

            string lines = GeneSequence;
            System.IO.File.WriteAllText("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\from_text_box.fasta", lines);
            
            if (GeneSequence != null)
            {
                input_file = "from_text_box.fasta";
            }
            
            var rand = RandomGen2.Next();
            Rand = rand;
            
            RunExtRamp(rand, tAI, rscu);

            // download file

            // check if only one bool is true
            bool[] outputFiles = { Vals, Speeds, NoRamps, RemovedSequences, AfterRamp, Standard };
            int numTrue = 0;
            foreach (bool outputFile in outputFiles)
            {
                if (outputFile == true)
                    numTrue += 1;
            }
            if (numTrue == 0 || numTrue == 1)
                return DownloadSingleFile(rand, input_file, tAI_file, rscu_file);
            else
                return DownloadFile(rand, input_file, tAI_file, rscu_file);
        }

        public ActionResult DownloadSingleFile(int rand, string uploaded_file, string uploaded_file_tAI, string uploaded_file_rscu)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory + "Output_files/";
            ViewData["path"] = path;

            //byte[] fileBytes = System.IO.File.ReadAllBytes(path + "ramp_output_" + rand + ".fasta");

            byte[] fileBytes; //= System.IO.File.ReadAllBytes(path + "ExtRamp_output_" + "ramp_sequences_" + rand + ".fasta");
            string fileName = "ExtRamp_output.fasta";

            
            if (Vals)
            {
                fileBytes = System.IO.File.ReadAllBytes(path + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".csv");
                fileName = "ExtRamp_output_" + "codon_efficiencies.csv";
            }
            else if (Speeds)
            {
                fileBytes = System.IO.File.ReadAllBytes(path + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".fasta");
                fileName = "ExtRamp_output_" + "codon_efficiencies.fasta";
            }
            else if (NoRamps)
            {
                fileBytes = System.IO.File.ReadAllBytes(path + "ExtRamp_output_" + "genes_without_ramps_" + rand + ".fasta");
                fileName = "ExtRamp_output_" + "genes_without_ramps.fasta";
            }
            else if (RemovedSequences)
            {
                fileBytes = System.IO.File.ReadAllBytes(path + "ExtRamp_output_" + "removed_sequences_" + rand + ".fasta");
                fileName = "ExtRamp_output_" + "removed_sequences.fasta";
            }
            else if (AfterRamp)
            {
                fileBytes = System.IO.File.ReadAllBytes(path + "ExtRamp_output_" + "gene_sequence_after_ramp_" + rand + ".fasta");
                fileName = "ExtRamp_output_" + "gene_sequence_after_ramp.fasta";
            }
            else
            {
                fileBytes = System.IO.File.ReadAllBytes(path + "ExtRamp_output_" + "ramp_sequences_" + rand + ".fasta");
                fileName = "ExtRamp_output_" + "ramp_sequences.fasta";
            }

            // Delete files
            System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".csv");
            System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".fasta");
            System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "genes_without_ramps_" + rand + ".fasta");
            System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "removed_sequences_" + rand + ".fasta");
            System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "gene_sequence_after_ramp_" + rand + ".fasta");
            System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "ramp_sequences_" + rand + ".fasta");
            if (uploaded_file != "example_input.fasta")
                System.IO.File.Delete("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file);
            if (uploaded_file_tAI != "none")
                System.IO.File.Delete("C:\\Users\\matthod\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file_tAI);
            if (uploaded_file_rscu != "none")
                System.IO.File.Delete("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file_rscu);


            return File(fileBytes, System.Net.Mime.MediaTypeNames.Application.Octet, fileName);

        }

        public ActionResult DownloadFile(int rand, string uploaded_file, string uploaded_file_tAI, string uploaded_file_rscu)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory + "Output_files/";
            ViewData["path"] = path;


            using (ZipFile zip = new ZipFile())
            {
                if (Vals)
                {
                    zip.AddFile(path + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".csv", "").FileName = "ExtRamp_output_" + "codon_efficiencies.csv";
                }
                if (Speeds)
                {
                    zip.AddFile(path + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".fasta", "").FileName = "ExtRamp_output_" + "codon_efficiencies.fasta";
                }
                if (NoRamps)
                {
                    zip.AddFile(path + "ExtRamp_output_" + "genes_without_ramps_" + rand + ".fasta", "").FileName = "ExtRamp_output_" + "genes_without_ramps.fasta";
                }
                if (RemovedSequences)
                {
                    zip.AddFile(path + "ExtRamp_output_" + "removed_sequences_" + rand + ".fasta", "").FileName = "ExtRamp_output_" + "removed_sequences.fasta";
                }
                if (AfterRamp)
                {
                    zip.AddFile(path + "ExtRamp_output_" + "gene_sequence_after_ramp_" + rand + ".fasta", "").FileName = "ExtRamp_output_" + "gene_sequence_after_ramp.fasta";
                }
                if (Standard)
                {
                    zip.AddFile(path + "ExtRamp_output_" + "ramp_sequences_" + rand + ".fasta", "").FileName = "ExtRamp_output_" + "ramp_sequences.fasta";
                }
                

                MemoryStream output = new MemoryStream();
                zip.Save(output);

                // Delete files
                System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".csv");
                System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".fasta");
                System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "genes_without_ramps_" + rand + ".fasta");
                System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "removed_sequences_" + rand + ".fasta");
                System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "gene_sequence_after_ramp_" + rand + ".fasta");
                System.IO.File.Delete(AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "ramp_sequences_" + rand + ".fasta");
                if (uploaded_file != "example_input.fasta")
                    System.IO.File.Delete("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file);
                if (uploaded_file_tAI != "none")
                    System.IO.File.Delete("C:\\Users\\matthod\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file_tAI);
                if (uploaded_file_rscu != "none")
                    System.IO.File.Delete("C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + uploaded_file_rscu);


                return File(output.ToArray(), "application/zip", "ExtRampOutput.zip");
            }

        }

        public static class RandomGen2
        {
            private static Random _global = new Random();
            [ThreadStatic]
            private static Random _local;

            public static int Next()
            {
                Random inst = _local;
                if (inst == null)
                {
                    int seed;
                    lock (_global) seed = _global.Next();
                    _local = inst = new Random(seed);
                }
                return inst.Next();
            }
        }

        public void RunExtRamp(int rand, bool tAI, bool rscu)
        {
            ViewData["file"] = "Uploads\\" + input_file;
            ViewData["status"] = rand;
            string progToRun = "C:\\Users\\matthodg\\ExtRamp.py";
            string args = " -i C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + input_file;
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "C:\\Users\\matthodg\\AppData\\Local\\Programs\\Python\\Python38\\python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;

            // call hello.py to concatenate passed parameters
            //proc.StartInfo.Arguments = string.Concat(progToRun, " ", x.ToString(), " ", y.ToString());
            //C:\\Users\\matthodgman\\HG00096_10

            if (tAI)
                args += " -a  C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + Upload_tAI.FileName;
            else if (Tissue != "none")
                args += " -a  C:\\Users\\matthodg\\tissue_tAI_values\\tAI_" + Tissue + ".csv";
            else
                args += " -a C:\\Users\\matthodg\\GRCh38_longest_isoforms.csv";

            if (rscu)
                args += " -u  C:\\Users\\matthodg\\source\\repos\\ExtRamp_ASP.Net\\ExtRamp_ASP.Net\\ExtRamp\\ExtRamp\\Uploads\\" + Upload_rscu.FileName;
            else
                args += " -u C:\\Users\\matthodg\\GRCh38_latest_genomic_longest_isoforms.fa";

            if (Vals)
                args += " -l " + AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".csv";
            if (Speeds)
                args += " -p " + AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "codon_efficiencies_" + rand + ".fasta";
            if (NoRamps)
                args += " -n " + AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "genes_without_ramps_" + rand + ".fasta";
            if (RemovedSequences)
                args += " -z " + AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "removed_sequences_" + rand + ".fasta";
            if (AfterRamp)
                args += " -x " + AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "gene_sequence_after_ramp_" + rand + ".fasta";
            if (Standard)
                args += " -o " + AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "ramp_sequences_" + rand + ".fasta";

            if (!Vals && !Speeds && !NoRamps && !RemovedSequences && !AfterRamp && !Standard)
                args += " -o " + AppDomain.CurrentDomain.BaseDirectory + "Output_files\\" + "ExtRamp_output_" + "ramp_sequences_" + rand + ".fasta";

            if (HasRNA)
                args += " -r ";
            if (WhichMean == "gmean")
                args += " -m gmean";
            if (WhichMean == "mean")
                args += " -m mean";
            if (WhichMean == "median")
                args += " -m median";
            if (RibosomeWindowLength != 9)
                args += " -w " + RibosomeWindowLength;
            if (BottleNeckLocation != 8)
                args += " -c " + BottleNeckLocation;
            if (MinSeqLen != 100)
                args += " -q " + MinSeqLen;

            Console.WriteLine(string.Concat(progToRun, args));

            proc.StartInfo.Arguments = string.Concat(progToRun, args);


            ViewData["test"] = AppDomain.CurrentDomain.BaseDirectory;
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            string stuff = "";

            foreach (string s in output)
                stuff += s;

            Console.WriteLine(stuff);

            //proc.WaitForExit();

            //Console.ReadLine();

            ViewData["result"] = stuff;
        }

        

        /*
        public void OnPost()
        {
            RunExtRamp();
            Message = "Done!";
        }
        */

    }
}