using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;

namespace ExtRamp.Pages
{
    public class ExtRampOnlineModel : PageModel
    {
        public SelectList ConsensusTissues { get; set; }
        public SelectList FantomTissues { get; set; }
        public SelectList HpaTissues { get; set; }
        public SelectList GtexTissues { get; set; }

        public SelectList Cells { get; set; }

        public void OnGet()
        {
            ConsensusTissues = new SelectList(new List<string>(new string[] { "none", "adiposetissue", "adrenalgland", "amygdala", "appendix", "basalganglia", "B-cells", "bonemarrow", "breast",
                "cerebellum", "cerebralcortex", "cervix_uterine", "colon", "corpuscallosum", "dendriticcells", "ductusdeferens", "duodenum", "endometrium", "epididymis", "esophagus",
                "fallopiantube", "gallbladder", "granulocytes", "heartmuscle", "hippocampalformation", "hypothalamus", "kidney", "liver", "lung", "lymphnode", "midbrain", "monocytes",
                "NK-cells", "olfactoryregion", "ovary", "pancreas", "parathyroidgland", "pituitarygland", "placenta", "ponsandmedulla", "prostate", "rectum", "retina", "salivarygland",
                "seminalvesicle", "skeletalmuscle", "skin", "smallintestine", "smoothmuscle", "spinalcord", "spleen", "stomach", "substantianigra", "T-cells", "testis", "thalamus",
                "thymus", "thyroidgland", "tongue", "tonsil", "totalPBMC", "urinarybladder", "vagina" }));

            FantomTissues = new SelectList(new List<string>(new string[] { "none", "adiposetissue", "amygdala", "appendix", "basalganglia", "breast", "cerebellum", "cerebralcortex",
                "cervix_uterine", "colon", "corpuscallosum", "ductusdeferens", "endometrium", "epididymis", "esophagus", "gallbladder", "heartmuscle",
                "hippocampalformation", "kidney", "liver", "lung", "lymphnode", "midbrain", "olfactoryregion", "ovary", "pancreas", "pituitarygland", "placenta",
                "ponsandmedulla", "prostate", "retina", "salivarygland", "seminalvesicle", "skeletalmuscle", "smallintestine", "smoothmuscle", "spinalcord", "spleen",
                "testis", "thalamus", "thymus", "thyroidgland", "tongue", "tonsil", "urinarybladder", "vagina" }));

            HpaTissues = new SelectList(new List<string>(new string[] { "none", "B-cells", "NK-cells", "T-cells", "adiposetissue", "adrenalgland", "appendix", "bonemarrow", 
                "breast", "cerebralcortex", "cervix_uterine", "colon", "dendriticcells", "duodenum", "endometrium", "epididymis", "esophagus", "fallopiantube", 
                "gallbladder", "granulocytes", "heartmuscle", "kidney", "liver", "lung", "lymphnode", "monocytes", "ovary", "pancreas", "parathyroidgland", "placenta",
                "prostate", "rectum", "salivarygland", "seminalvesicle", "skeletalmuscle", "skin", "smallintestine", "smoothmuscle", "spleen", "stomach", "testis", 
                "thyroidgland", "tonsil", "urinarybladder" }));

            GtexTissues = new SelectList(new List<string>(new string[] { "none", "adiposetissue", "adrenalgland", "amygdala", "basalganglia", "breast", "cerebellum", 
                "cerebralcortex", "cervix_uterine", "colon", "endometrium", "esophagus", "fallopiantube", "heartmuscle", "hippocampalformation", "hypothalamus",
                "kidney", "liver", "lung", "midbrain", "ovary", "pancreas", "pituitarygland", "prostate", "salivarygland", "skeletalmuscle", "skin", "smallintestine",
                "spinalcord", "spleen", "stomach", "testis", "thyroidgland", "urinarybladder", "vagina" }));

            Cells = new SelectList(new List<string>(new string[] { "adrenal_gland__glandular_cells", "appendix__glandular_cells", "appendix__lymphoid_tissue", 
                "bone_marrow__hematopoietic_cells", "breast__glandular_cells", "breast__myoepithelial_cells", "bronchus__respiratory_epithelial_cells", "caudate__glial_cells", 
                "caudate__neuronal_cells", "cerebellum__cells_in_granular_layer", "cerebellum__cells_in_molecular_layer", "cerebellum__Purkinje_cells", "cerebral_cortex__glial_cells", 
                "cerebral_cortex__neuronal_cells", "cervix_uterine__glandular_cells", "cervix_uterine__squamous_epithelial_cells", "colon__endothelial_cells", "colon__glandular_cells",
                "colon__peripheral_nerve_or_ganglion", "duodenum__glandular_cells", "endometrium_1__glandular_cells", "endometrium_2__glandular_cells", "epididymis__glandular_cells", 
                "esophagus__squamous_epithelial_cells", "fallopian_tube__glandular_cells", "gallbladder__glandular_cells", "heart_muscle__myocytes", "hippocampus__glial_cells", 
                "hippocampus__neuronal_cells", "kidney__cells_in_glomeruli", "kidney__cells_in_tubules", "liver__hepatocytes", "lung__macrophages", "lung__pneumocytes", 
                "lymph_node__germinal_center_cells", "lymph_node__non-germinal_center_cells", "nasopharynx__respiratory_epithelial_cells", "oral_mucosa__squamous_epithelial_cells",
                "pancreas__exocrine_glandular_cells", "pancreas__islets_of_Langerhans", "parathyroid_gland__glandular_cells", "placenta__decidual_cells", "placenta__trophoblastic_cells",
                "prostate__glandular_cells", "rectum__glandular_cells", "salivary_gland__glandular_cells", "seminal_vesicle__glandular_cells", "skin_1__fibroblasts", "skin_1__keratinocytes", 
                "skin_1__Langerhans", "skin_1__melanocytes", "skin_2__epidermal_cells", "small_intestine__glandular_cells", "soft_tissue_1__fibroblasts", "spleen__cells_in_red_pulp", 
                "spleen__cells_in_white_pulp", "stomach_1__glandular_cells", "stomach_2__glandular_cells", "testis__cells_in_seminiferous_ducts", "testis__Leydig_cells",
                "thyroid_gland__glandular_cells", "tonsil__germinal_center_cells", "tonsil__non-germinal_center_cells", "tonsil__squamous_epithelial_cells", "urinary_bladder__urothelial_cells",
                "vagina__squamous_epithelial_cells" }));
        }
    }
}