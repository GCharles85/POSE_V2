namespace Diagnoses.Models
{
    public class DiagnosticItem
    {
        public int Id { get; set; }  // Primary key

        public string Title { get; set; }
        public string Cost { get; set; }
        public string Description { get; set; }
        public string Icon { get; set; }
    }
}
