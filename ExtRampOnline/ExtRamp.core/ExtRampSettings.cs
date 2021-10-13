using System;
using System.Collections.Generic;
using System.Text;


namespace ExtRamp.core
{
    public class ExtRampSettings
    {
        public bool HasRna { get; set; }
        public int MinimumSequenceLength { get; set; }
        public int RibosomeWindowLength { get; set; }
        public int BottleneckLocation { get; set; }
        public MeanAnalysis Mean { get; set; }
         
    }
}
